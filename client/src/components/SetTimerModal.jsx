import React from "react";
import { X } from "lucide-react";

const SetTimerModal = ({ isOpen, onClose, onSetTimer }) => {
  const [minutes, setMinutes] = React.useState(3);
  const [seconds, setSeconds] = React.useState(2);

  if (!isOpen) return null;

  const handleSubmit = (e) => {
    e.preventDefault();
    onSetTimer(minutes, seconds);
    onClose();
  };

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center">
      <div className="bg-white rounded-lg p-8 w-[400px] relative">
        <button
          onClick={onClose}
          className="absolute right-4 top-4 text-gray-500 hover:text-gray-700"
        >
          <X size={24} />
        </button>

        <h2 className="text-3xl font-bold text-center mb-4">Set Timer</h2>
        <p className="text-center text-gray-600 mb-6">
          Each task can have its own allocated voting time.
        </p>

        <form onSubmit={handleSubmit}>
          <div className="flex justify-center gap-2 mb-8">
            <div className="w-20 text-center">
              <select
                value={minutes}
                onChange={(e) => setMinutes(Number(e.target.value))}
                className="w-full p-2 border rounded-lg text-2xl text-center bg-gray-50"
              >
                {Array.from({ length: 6 }, (_, i) => (
                  <option key={i} value={i}>
                    {String(i).padStart(2, "0")}
                  </option>
                ))}
              </select>
            </div>
            <span className="text-2xl flex items-center">:</span>
            <div className="w-20 text-center">
              <select
                value={seconds}
                onChange={(e) => setSeconds(Number(e.target.value))}
                className="w-full p-2 border rounded-lg text-2xl text-center bg-gray-50"
              >
                {Array.from({ length: 60 }, (_, i) => (
                  <option key={i} value={i}>
                    {String(i).padStart(2, "0")}
                  </option>
                ))}
              </select>
            </div>
          </div>

          <div className="flex justify-end gap-4">
            <button
              type="button"
              onClick={onClose}
              className="px-6 py-2 text-gray-600 hover:bg-gray-100 rounded-lg"
            >
              Cancel
            </button>
            <button
              type="submit"
              className="px-6 py-2 bg-teal-600 text-white rounded-lg hover:bg-teal-700"
            >
              OK
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default SetTimerModal;
