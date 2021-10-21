import {
  BrowserRouter as Router,
  Switch,
  Route,
} from "react-router-dom";
import Header from '../components/Header/Header'
import Footer from '../components/Footer/Footer'
import Border from '../components/Border/Border'
import DropArea from '../components/DropArea/DropArea'
import React  from 'react';
import './App.css'


function App() {
  return (
    
    <Router>
      <div className="App">
          <Header />
          <Border />
          <Footer />
        <Switch>
          <Route path="/DropArea">
            <DropArea />
          </Route>
        </Switch>
      </div>
    </Router>
    );
}

export default App;
