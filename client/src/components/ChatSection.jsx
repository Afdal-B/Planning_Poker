import React, { useState } from "react";
import { Send } from "lucide-react";

const ChatSection = () => {
  const [message, setMessage] = useState("");
  const [messages] = useState([
    {
      id: 1,
      user: "Annie Haley",
      avatar:
        "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80",
      content:
        "Welcome everyone! We will vote for the first task to take it as a reference",
      timestamp: "19:19",
    },
  ]);

  const handleSubmit = (e) => {
    e.preventDefault();
    // Handle message submission
    setMessage("");
  };

  return (
    <div className="border-t mt-auto">
      <div className="p-4">
        <h3 className="font-semibold mb-4">Messages</h3>
        <div className="space-y-4 max-h-60 overflow-y-auto">
          {messages.map((msg) => (
            <div key={msg.id} className="flex items-start gap-3">
              <img
                src={msg.avatar}
                alt={msg.user}
                className="w-8 h-8 rounded-full"
              />
              <div>
                <div className="flex items-center gap-2">
                  <span className="font-medium">{msg.user}</span>
                  <span className="text-sm text-gray-500">{msg.timestamp}</span>
                </div>
                <p className="text-gray-700">{msg.content}</p>
              </div>
            </div>
          ))}
        </div>
      </div>
      <form onSubmit={handleSubmit} className="p-4 border-t flex gap-2">
        <input
          type="text"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Type a message..."
          className="flex-1 px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
        <button
          type="submit"
          className="p-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600"
        >
          <Send size={20} />
        </button>
      </form>
    </div>
  );
};

export default ChatSection;
