import LandingPage from "./pages/LandingPage";
import CreateRoomPage from "./pages/CreateRoomPage";
import JoinRoomPage from "./pages/JoinRoomPage";
import UserInfosPage from "./pages/UserInfosPage";
import { Routes, Route } from "react-router-dom";
export default function App() {
  return (
    <div>
      <CreateRoomPage></CreateRoomPage>
      {/*<Routes>
      <Route path="/" element={<LandingPage />} />
      <Route path="/create-room" element={<CreateRoomPage />} />
      <Route path="/join-room" element={<JoinRoomPage />} />
      <Route path="/profile" element={<UserInfosPage />} />
    </Routes>*/}
    </div>
  );
}
