import Header from '../components/layout/Header/Header'
import Footer from '../components/layout/Footer/Footer'
import Border from '../components/Steps/Steps'
import DropArea from '../components/DropArea/DropArea'
import MainContainer from '../components/layout/MainContainer/MainContainer'
import MainContent from '../components/layout/MainContent/MainContent'
import "/home/daniapm/tributi/final_project_tributi/Nomis_react/src/assets/static/logo.jpg"


function App() {
  return (
    <MainContainer>
      <Header />
      <MainContent>
        <Border />
      </MainContent>
      <Footer/>
    </MainContainer>
    );
}

export default App;
