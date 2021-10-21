import {
  BrowserRouter as Router,
  Switch,
  Route,
} from "react-router-dom";
import Header from '../components/layout/Header/Header'
import Footer from '../components/layout/Footer/Footer'
import Border from '../components/Steps/Steps'
import DropArea from '../components/DropArea/DropArea'
import TaxFile from '../components/TaxFile/TaxFile'
import UpdateDump from '../components/UpdateDump/UpdateDump'
import Mathops from '../components/Mathops/Mathops'
import LightweightFile from '../components/LightweightFile/LightweightFile'
import ConfigFile from '../components/ConfigFile/ConfigFile'
import MainContainer from '../components/layout/MainContainer/MainContainer'
import MainContent from '../components/layout/MainContent/MainContent'
import "../assets/static/logo (3).jpg"


function App() {
  return (

    <MainContainer>
      <Header />
        <Router>
          <MainContent>
            <Switch>
              <Border />
              <Router path="/TaxFile">
                <TaxFile />
              </Router>
              <Router path="/UpdateDump">
                <UpdateDump />
              </Router>
              <Router path="/Mathops">
                <Mathops />
              </Router>
              <Router path="/LightweightFile">
                <LightweightFile />
              </Router>
              <Router path="/ConfigFile">
                <ConfigFile />
              </Router>
            </Switch>
          </MainContent>
        </Router>
      <Footer/>
    </MainContainer>
    );
}

export default App;
