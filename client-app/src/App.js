import {Routes, Route, BrowserRouter} from 'react-router-dom';
import {useState, useEffect} from 'react';
import {Navbar} from './components/components'
import {HomePage, LoginPage, ProfilePage, SignUpPage} from './pages/pages'
import './App.css';
import TestPage from './pages/TestPage';
import Axios from 'axios'

function App() {
  const [loginStatus, setLoginStatus] = useState(false)

  useEffect(() => {
    Axios.get('http://127.0.0.1:5000')
  },[])
  return (
    <BrowserRouter>
    <Navbar loginStatus={loginStatus}/>
    <Routes>
      <Route path='/' element={<HomePage/>}></Route>
      <Route path='/test' element={<TestPage/>}></Route>
      <Route path='/login' element={<LoginPage setLoginStatus={setLoginStatus}/>}></Route>
      <Route path='/signup' element={<SignUpPage/>}></Route>
      <Route path='/profile' element={<ProfilePage/>}></Route>
    </Routes>

    </BrowserRouter>
  );
}

export default App;
