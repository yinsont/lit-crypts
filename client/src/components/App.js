import React from "react";
import { BrowserRouter as Router, Switch, Route, Link} from "react-router-dom";
import Home from "./Home.js"
import About from "./About.js"
function App() {
 return (
    <div className="app">
      <nav className="navbar">
        <Link className='link' to='/' exact="true">Home</Link>
        <br/>
        <Link className='link' to='/' exact="true">About</Link>
        <br/>
      </nav>
      <Router>
        <Switch>
          <Route path="/"><Home /></Route>
          <Route path="*"><About/></Route>
        </Switch>
      </Router>
    </div>
  );
}

export default App;
