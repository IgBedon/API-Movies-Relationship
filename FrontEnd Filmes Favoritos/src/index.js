//bibliotecas
import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
//paginas
import Home from './components/pages/Home'
//componentes
import Navbar from './components/layout/Navbar';
import Footer from './components/layout/Footer'

const rootElement = document.getElementById('root');

ReactDOM.render(
  <Router>
    <Navbar/>
    <Routes>
      <Route path="/home" element={<Home />} />
    </Routes>
    <Footer/>
  </Router>,
  rootElement
);
