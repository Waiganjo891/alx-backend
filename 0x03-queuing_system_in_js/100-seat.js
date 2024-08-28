const express = require('express');
const redis = require('redis');
const { promisify } = require('util');
const kue = require('kue');

const client = redis.createClient();
const reserveSeat = promisify(client.set).bind(client);
const getCurrentAvailableSeats = promisify(client.get).bind(client);

const queue = kue.createQueue();

const app = express();
const port = 1245;

let reservationEnabled = true;

const initialSeats = 50;
async function initializeSeats() {
  await reserveSeat('available_seats', initialSeats);
}

initializeSeats();

app.get('/available_seats', async (req, res) => {
  try {
    const seats = await getCurrentAvailableSeats('available_seats');
    res.json({ numberOfAvailableSeats: seats });
  } catch (error) {
    res.status(500).json({ error: 'Unable to retrieve available seats' });
  }
});

app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservations are blocked' });
  }
  const job = queue.create('reserve_seat').save((err) => {
    if (err) {
      return res.status(500).json({ status: 'Reservation failed' });
    }
    res.json({ status: 'Reservation in process' });
  });
  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  }).on('failed', (errorMessage) => {
    console.log(`Seat reservation job ${job.id} failed: ${errorMessage}`);
  });
});

app.get('/process', (req, res) => {
  res.json({ status: 'Queue processing' });
  queue.process('reserve_seat', async (job, done) => {
    try {
      let availableSeats = await getCurrentAvailableSeats('available_seats');
      availableSeats = parseInt(availableSeats);
      if (availableSeats > 0) {
        availableSeats -= 1;
        await reserveSeat('available_seats', availableSeats);
        if (availableSeats === 0) {
          reservationEnabled = false;
        }
        done();
      } else {
        done(new Error('Not enough seats available'));
      }
    } catch (error) {
      done(new Error('Reservation process failed'));
    }
  });
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
