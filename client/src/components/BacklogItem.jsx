const BacklogItem = ({ check, _id, en_tant_que, fonctionnalite, objectif, action }) => {
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
      <div className="text-center font-medium">{_id}</div>
      <div className="text-center">{en_tant_que}</div>
      <div className="col-span-2 text-center">{fonctionnalite}</div>
      <div className="text-center">{objectif}</div>
      <div className="flex justify-center">
        <button className="px-4 py-1 bg-blue-500 text-white rounded hover:bg-blue-600">
          {action}
        </button>
      </div>
    </div>
  );
};
export default BacklogItem;
