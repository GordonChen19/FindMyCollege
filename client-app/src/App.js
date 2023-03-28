import {Routes, Route, BrowserRouter} from 'react-router-dom';
import {useState} from 'react';
import {Navbar} from './components/components'
import {HomePage, LoginPage, ProfilePage, SignUpPage} from './pages/pages'
import './App.css';
import TestPage from './pages/TestPage';

function App() {
  const [loginStatus, setLoginStatus] = useState(false)

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
