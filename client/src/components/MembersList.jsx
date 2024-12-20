import React from "react";

const MembersList = ({ members }) => {
  return (
    <div className="p-4 border-l w-80 overflow-y-auto">
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
              <p className="font-medium">{member.username}</p>
              <p className="text-sm text-gray-500">Joined</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default MembersList;
