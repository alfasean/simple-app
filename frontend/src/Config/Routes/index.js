import React from 'react'
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom'
import {Home, Login, Regis} from '../../Pages'

const Index = () => {
    return (
      <Router>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/regis" element={<Regis />} />
          <Route path="/login" element={<Login />} />
        </Routes>
      </Router>
    );
  }

export default Index;
