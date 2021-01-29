const app = require('express')();
const http = require('http').Server(app);
const io = require('socket.io')(http);

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});
//wysyłanie wiadomości do wszystkich dostępnych użytkowników
io.on('connection', (socket) => {
    socket.on('chat message', (msg) => {
        io.emit('chat message', msg);
      });
});
 
// wybór portu na którym nasłuchuje serwer
http.listen(3000, () => {
  console.log('listening on *:3000');
});