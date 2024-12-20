import React, { useEffect, useState } from "react";
import { io } from "socket.io-client";
import { API_URL } from "../constants/constants";

const socket = io(API_URL); // Connexion au serveur Flask-SocketIO

const Timer = () => {
  const [remainingTime, setRemainingTime] = useState(null);

  useEffect(() => {
    // Écouter les événements du timer
    socket.on('timer_update', (data) => {
      setRemainingTime(data.remaining_time);
    });

    socket.on('timer_expired', (data) => {
      alert(data.message); // Affiche une alerte lorsque le timer expire
    });

    return () => {
      socket.off('timer_update');
      socket.off('timer_expired');
    };
  }, []);

  const startTimer = () => {
    socket.emit('start_timer', { room_code: 'room1', duration: 30 });
  };

  return (
    <div>
      <h1>Remaining Time: {remainingTime !== null ? remainingTime : 'N/A'}</h1>
      <button onClick={startTimer}>Start Timer</button>
    </div>
  );
};

export default Timer;


/*{const Timer = () => {
  const [time, setTime] = useState(0);

  useEffect(() => {
    // Écoute l'événement "update_time" pour recevoir le temps
    socket.on("update_time", (data) => {
      setTime(data.time);
    });

    // Nettoyer l'écouteur à la déconnexion
    return () => {
      socket.off("update_time");
    };
  }, []);

  // Formater le temps en MM:SS
  const formatTime = (seconds) => {
    const minutes = Math.floor(seconds / 60);
    const remainingSeconds = seconds % 60;
    return `${String(minutes).padStart(2, "0")}:${String(
      remainingSeconds
    ).padStart(2, "0")}`;
  };

  return (
    <div className="flex items-center justify-center bg-[#ECF4F7FF] text-white p-4 rounded-md shadow-md w-20">
      <h1 className="text-xl font-mono font-semibold text-[#378C9FFF]">
        {formatTime(time)}
      </h1>
    </div>
  );
};

export default Timer;}
*/