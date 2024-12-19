import React from "react";

const FeatureListItem = ({ number, actor, feature, goal }) => {
  return (
    <div className="grid grid-rows-2 grid-cols-2 gap-8 p-4">
      <div className="bg-[#ECF4F7FF] h-[100px] w-[175px] p-8 rounded-lg shadow-md flex flex-col items-center justify-center">
        <div className="font-medium text-gray-500 mb-2">Numéro</div>
        <div className="font-bold">{number}</div>
      </div>
      <div className="bg-[#ECF4F7FF] h-[100px] w-[175px] p-8 rounded-lg shadow-md flex flex-col items-center justify-center">
        <div className="font-medium text-gray-500 mb-2">Acteur</div>
        <div className="font-bold">{actor}</div>
      </div>
      <div className="bg-[#ECF4F7FF] h-[100px] w-[175px] p-8 rounded-lg shadow-md flex flex-col items-center justify-center">
        <div className="font-medium text-gray-500 mb-2">Fonctionnalité</div>
        <div className="font-bold ">{feature}</div>
      </div>
      <div className="bg-[#ECF4F7FF] h-[100px] w-[175px] p-8 rounded-lg shadow-md flex flex-col items-center justify-center">
        <div className="font-medium text-gray-500 mb-2">Objectif</div>
        <div className="font-bold">{goal}</div>
      </div>
    </div>
  );
};

export default FeatureListItem;
