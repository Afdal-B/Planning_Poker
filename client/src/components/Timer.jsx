import React, { useEffect, useState } from "react";
import { io } from "socket.io-client";

const socket = io("http://localhost:5000"); // Connexion au serveur Flask-SocketIO

const Timer = () => {
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
    <div className="flex items-center justify-center bg-gray-800 text-white p-4 rounded-md shadow-md">
      <h1 className="text-3xl font-mono font-semibold">{formatTime(time)}</h1>
    </div>
  );
};

export default Timer;
