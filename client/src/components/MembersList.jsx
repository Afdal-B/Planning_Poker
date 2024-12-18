import React from "react";

const MembersList = () => {
  const members = [
    {
      id: 1,
      name: "Adam Murphy",
      avatar:
        "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80",
      status: "Joined room",
    },
    // Add more members as needed
  ];

  return (
    <div className="p-4 border-l w-80">
      <h3 className="font-semibold mb-4">Members</h3>
      <div className="space-y-4">
        {members.map((member) => (
          <div key={member.id} className="flex items-center gap-3">
            <img
              src={member.avatar}
              alt={member.name}
              className="w-10 h-10 rounded-full"
            />
            <div>
              <p className="font-medium">{member.name}</p>
              <p className="text-sm text-gray-500">{member.status}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default MembersList;
