import { createContext, useState } from 'react';
import './App.css';
import { Routes, Route } from 'react-router-dom';
import Home from './Components/Home';
import Header from './Components/Header';
import SignUp from './Components/SignUp';
import Login from './Components/Login';
import Courses from './Components/Courses';
import Cart from './Components/Cart';
import ProtectedRoute from './Components/ProtectedRoute';
export const AppContext = createContext();

function App() {
  const accessToken = localStorage.getItem('access');
  const isAuthenticated = accessToken ? true : false;
  const [signedIn, setSignedIn] = useState(false);

  return (
    <>
      <AppContext.Provider value={{isAuthenticated, signedIn, setSignedIn}}>
        <Header />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/signup" element={<SignUp />} />
          <Route path="/login" element={<Login />} />
          <Route 
            path="/courses" 
            element={
            <ProtectedRoute>
              <Courses />
            </ProtectedRoute>
            } 
          />
          <Route
            path='/cart'
            element={
              <ProtectedRoute>
                <Cart />
              </ProtectedRoute>
            }
          />
        </Routes>
      </AppContext.Provider>
    </>
  );
}

export default App;
