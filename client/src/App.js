import LandingPage from "./pages/LandingPage";
import CreateRoomPage from "./pages/CreateRoomPage";
import JoinRoomPage from "./pages/JoinRoomPage";
import UserInfosPage from "./pages/UserInfosPage";
import InvitationPage from "./pages/InvitationPage";
import VotingPage from "./pages/VotingPage";
import { Routes, Route, BrowserRouter } from "react-router";
import VotingPageUser from "./pages/VotingPageUser";
export default function App() {
  return (
    <div>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<LandingPage />} />
          <Route path="/create-room" element={<CreateRoomPage />} />
          <Route path="/join-room" element={<JoinRoomPage />} />
          <Route path="/profile" element={<UserInfosPage />} />
          <Route path="/invitation" element={<InvitationPage />} />
          <Route path="/voting" element={<VotingPage />} />
          <Route path="/voting-page-user" element={<VotingPageUser />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}
