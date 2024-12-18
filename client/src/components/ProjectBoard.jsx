import React from "react";
import BacklogTable from "./BacklogTable";
import MembersList from "./MembersList";
import ChatSection from "./ChatSection";

function ProjectBoard() {
  return (
    <div className="min-h-screen bg-white">
      <div className="flex h-screen">
        <div className="flex-1 flex flex-col">
          <div className="p-6 flex-1 overflow-auto">
            <BacklogTable />
          </div>
        </div>
        <div className="w-80 flex flex-col border-l">
          <MembersList />
          <ChatSection />
        </div>
      </div>
    </div>
  );
}

export default ProjectBoard;
