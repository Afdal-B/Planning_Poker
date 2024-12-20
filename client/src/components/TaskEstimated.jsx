import React,{useState} from "react";
const TaskEstimated = ({ open,value}) => {
const [isOpen,setIsOpen] = useState(open);
  if (!isOpen) return null; // Ne rien afficher si `open` est false

  return (
    <div className="fixed inset-0 bg-gray-800 bg-opacity-50 flex items-center justify-center z-50">
      <div className="bg-white rounded-lg shadow-lg max-w-md w-full p-6">
        {/* Contenu de la modale */}
        <div className="text-center">
          <div className="bg-green-100 text-green-600 w-10 h-10 flex items-center justify-center mx-auto rounded-full mb-4">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              className="h-6 w-6"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M5 13l4 4L19 7"
              />
            </svg>
          </div>
          <h2 className="text-2xl font-bold mb-2">Task Estimated</h2>
          <p className="text-gray-600 mb-6">
            This backlog task has been assessed with a difficulty rating of {value}
            <span className="font-bold">5</span>.
          </p>
          {/* Bouton pour fermer la modale */}
          <button
            onClick={()=>{setIsOpen(false)}}
            className="flex items-center justify-center gap-2 px-6 py-3 bg-blue-500 text-white font-bold rounded-lg shadow-lg hover:bg-blue-600 transition"
          >
            Next Task
            <svg
              xmlns="http://www.w3.org/2000/svg"
              className="h-5 w-5"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M13 7l5 5m0 0l-5 5m5-5H6"
              />
            </svg>
          </button>
        </div>
      </div>
    </div>
  );
};

export default TaskEstimated;
