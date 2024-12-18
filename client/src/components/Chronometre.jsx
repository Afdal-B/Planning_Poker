import React, { useEffect, useState } from "react";
import { io } from "socket.io-client";
import { API_URL } from "../constants/constants";

const socket = io(API_URL); // Connexion au serveur Flask-SocketIO

const Chronometer = () => {
  const [time, setTime] = useState(0);

  useEffect(() => {
    // Écoute l'événement 'update_time' envoyé par le serveur
    socket.on("update_time", (data) => {
      setTime(data.time);
    });

    // Nettoyage à la déconnexion
    return () => {
      socket.off("update_time");
    };
  }, []);

  // Fonction pour formater le temps (minutes:secondes)
  const formatTime = (seconds) => {
    const minutes = Math.floor(seconds / 60);
    const remainingSeconds = seconds % 60;
    return `${String(minutes).padStart(2, "0")}:${String(
      remainingSeconds
    ).padStart(2, "0")}`;
  };

  // Envoyer des événements de contrôle au serveur
  const startTimer = () => socket.emit("start_timer");
  const stopTimer = () => socket.emit("stop_timer");

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-900 text-white">
      <h1 className="text-4xl font-bold mb-4">⏱ Chronomètre Synchronisé</h1>
      <div className="text-6xl font-mono bg-gray-800 p-6 rounded-lg shadow-lg">
        {formatTime(time)}
      </div>
      <div className="mt-6 flex space-x-4">
        <button
          onClick={startTimer}
          className="px-4 py-2 bg-green-500 hover:bg-green-600 text-white font-semibold rounded"
        >
          Démarrer
        </button>
        <button
          onClick={stopTimer}
          className="px-4 py-2 bg-red-500 hover:bg-red-600 text-white font-semibold rounded"
        >
          Arrêter
        </button>
      </div>
    </div>
  );
};

export default Chronometer;
