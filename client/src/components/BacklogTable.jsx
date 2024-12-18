import React, { useState } from "react";
import { Check } from "lucide-react";

const BacklogTable = ({ backlogItems: initialBacklogItems }) => {
  const [backlogItems, setBacklogItems] = useState(initialBacklogItems || []);

  const toggleCheck = (id) => {
    setBacklogItems(
      backlogItems.map((item) =>
        item.id === id ? { ...item, checked: !item.checked } : item
      )
    );
  };

  return (
    <div className="mt-6">
      <div className="flex justify-between items-center mb-4">
        <h2 className="text-xl font-semibold">Backlog items</h2>
        <span className="text-gray-600">
          Total <span className="text-blue-500">{backlogItems.length}</span>{" "}
          items
        </span>
      </div>
      <div className="overflow-x-auto">
        <table className="w-full">
          <thead>
            <tr className="text-left border-b">
              <th className="p-4">Check</th>
              <th className="p-4">ID</th>
              <th className="p-4">Actor</th>
              <th className="p-4">Feature</th>
              <th className="p-4">Goal</th>
              <th className="p-4">Action</th>
            </tr>
          </thead>
          <tbody>
            {backlogItems.map((item) => (
              <tr key={item.id} className="border-b hover:bg-gray-50">
                <td className="p-4">
                  <div
                    onClick={() => toggleCheck(item.id)}
                    className="w-5 h-5 border rounded flex items-center justify-center cursor-pointer hover:bg-gray-100"
                  >
                    {item.checked && (
                      <Check size={16} className="text-blue-500" />
                    )}
                  </div>
                </td>
                <td className="p-4">{item.id}</td>
                <td className="p-4">{item.actor}</td>
                <td className="p-4">{item.feature}</td>
                <td className="p-4">{item.goal}</td>
                <td className="p-4">
                  <button className="bg-blue-500 text-white px-4 py-1 rounded hover:bg-blue-600">
                    Vote
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default BacklogTable;
