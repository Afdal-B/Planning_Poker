const MessageBox = ({ message }) => {
  return (
    <div className="flex flex-col bg-gray-100 p-3 rounded-md">
      <span className="text-sm font-semibold mb-1">{message.sender}</span>
      <span className="text-sm text-gray-700">{message.content}</span>
    </div>
  );
};
export default MessageBox;
