const BacklogItem = ({ check, id, actor, feature, goal, action }) => {
  return (
    <div className="grid grid-cols-6 items-center border-b py-4">
      <div className="flex justify-center">
        <input
          type="checkbox"
          checked={check}
          className="h-5 w-5 text-blue-600 rounded"
          readOnly
        />
      </div>
      <div className="text-center font-medium">{id}</div>
      <div className="text-center">{actor}</div>
      <div className="col-span-2 text-center">{feature}</div>
      <div className="text-center">{goal}</div>
      <div className="flex justify-center">
        <button className="px-4 py-1 bg-blue-500 text-white rounded hover:bg-blue-600">
          {action}
        </button>
      </div>
    </div>
  );
};
export default BacklogItem;
