import React, { useState, useEffect } from "react";
import { Timer as TimerIcon, Settings } from "lucide-react";
import SetTimerModal from "./SetTimerModal";

const Timer = () => {
  const [timeLeft, setTimeLeft] = React.useState(0);
  const [isRunning, setIsRunning] = React.useState(false);
  const [showModal, setShowModal] = React.useState(false);

  useEffect(() => {
    let interval;
    if (isRunning && timeLeft > 0) {
      interval = setInterval(() => setTimeLeft((t) => t - 1), 1000);
    } else if (timeLeft === 0) {
      setIsRunning(false);
    }
    return () => clearInterval(interval);
  }, [isRunning, timeLeft]);

  const formatTime = (s) =>
    `${String(Math.floor(s / 60)).padStart(2, "0")}:${String(s % 60).padStart(
      2,
      "0"
    )}`;

  return (
    <div className="flex flex-col items-center">
      <div className="bg-white rounded-lg shadow p-3 w-[100px]">
        <div className="flex justify-between items-center mb-1">
          <TimerIcon className="text-teal-600" size={12} />
          <button
            onClick={() => setShowModal(true)}
            className="text-gray-400 hover:text-gray-600"
          >
            <Settings size={10} />
          </button>
        </div>

        <div className="text-2xl font-bold text-center mb-2 font-mono">
          {formatTime(timeLeft)}
        </div>

        <button
          onClick={() => {
            timeLeft === 0 ? setShowModal(true) : setIsRunning(!isRunning);
          }}
          className={`w-full py-1 rounded text-white text-xs font-medium transition-colors ${
            isRunning
              ? "bg-red-500 hover:bg-red-600"
              : "bg-teal-600 hover:bg-teal-700"
          }`}
        >
          {isRunning ? "Stop" : timeLeft === 0 ? "Set Timer" : "Start"}
        </button>
      </div>

      <SetTimerModal
        isOpen={showModal}
        onClose={() => setShowModal(false)}
        onSetTimer={(m, s) => setTimeLeft(m * 60 + s)}
      />
    </div>
  );
};

export default Timer;
