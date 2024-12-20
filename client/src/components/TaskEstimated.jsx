import React from "react";
import Modal from "react-modal";
import { Check } from "lucide-react";

const TaskEstimated = ({ isOpen, onClose, difficulty, onNextTask }) => {
  return (
    <Modal
      isOpen={isOpen}
      onRequestClose={onClose}
      className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 bg-white rounded-3xl p-12 w-[500px] outline-none"
      overlayClassName="fixed inset-0 bg-black bg-opacity-50"
    >
      <div className="flex flex-col items-center">
        <div className="mb-6">
          <div className="w-12 h-12 bg-teal-50 rounded-full flex items-center justify-center">
            <Check className="w-6 h-6 text-teal-600" />
          </div>
        </div>

        <h2 className="text-4xl font-bold mb-6">Task Estimated</h2>

        <p className="text-gray-600 text-center text-lg mb-8">
          This backlog task has been assessed with a difficulty rating of{" "}
          <span className="font-semibold">{difficulty}</span>
        </p>

        <button
          onClick={onNextTask}
          className="bg-teal-600 text-white px-6 py-3 rounded-lg font-medium hover:bg-teal-700 transition-colors flex items-center gap-2"
        >
          Next task
          <span className="inline-block transform -rotate-45">↓</span>
        </button>
      </div>
    </Modal>
  );
};

export default TaskEstimated;
