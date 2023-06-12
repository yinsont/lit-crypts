import { React } from "react";
import { Link } from "react-router-dom";

export default function Dropdown() {
  return (
      <nav className = "Dropdown-Menu">
            <Link className="link" to="/home" exact="true">
            Home
            </Link>
            <Link className="link" to="/about" exact="true">
            About
            </Link>
            <Link className="link" to="/signup" exact="true">
            Sign-up/Login
            </Link>
            <Link className="link" to="/leaderboard" exact="true">
            Leaderboard
            </Link>

      </nav>
      );
    }
    