import Header from '../components/layout/Header/Header'
import Footer from '../components/layout/Footer/Footer'
import DropArea from '../components/DropArea/DropArea'
import MainContainer from '../components/layout/MainContainer/MainContainer'
import MainContent from '../components/layout/MainContent/MainContent'
import "/home/daniapm/tributi/final_project_tributi/Nomis_react/src/assets/static/logo.jpg"
import StepComponent from '../components/Steps/Steps'


function App() {
  return (
    <MainContainer>
      <Header />
      <MainContent>
        <StepComponent />
      </MainContent>
      <Footer/>
    </MainContainer>
    );
}

export default App;
