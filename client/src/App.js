import './App.css';
import { Routes, Route } from 'react-router-dom';
import Home from './Components/Home';
import Header from './Components/Header';
import SignUp from './Components/SignUp';
import Login from './Components/Login';
import Courses from './Components/Courses';
import Cart from './Components/Cart';

function App() {
  return (
    <>
      <Header />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/signup" element={<SignUp />} />
        <Route path="/login" element={<Login />} />
        <Route path="/courses" element={<Courses />} />
      </Routes>
      <Cart></Cart>
    </>
  );
}

export default App;
