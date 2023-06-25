import React, { useState } from "react";
import { Link } from "react-router-dom";

export default function Signup({ onLogin }) {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const [passwordConfirmation, setPasswordConfirmation] = useState("");

  const [errors, setErrors] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  function handleSubmit(e) {
    e.preventDefault();
    setIsLoading(true);
    fetch("http://127.0.0.1:5555/users", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        user: {
          username,
          email,
          password,
        },
      }),
    }).then((r) => {
      setIsLoading(false);
      // debugger
      if (r.ok) {
        r.json().then((user) => onLogin(user));
      } else {
        r.json().then((err) => setErrors(err.errors));
      }
    });
  }

  function handleChange(e) {
    console.log(e.target.name);
    switch (e.target.name) {
      case "username":
        setUsername(e.target.value);
        break;
      case "email":
        setEmail(e.target.value);
        break;
      case "password":
        setPassword(e.target.value);
        break;
      case "passwordConfirmation":
        setPasswordConfirmation(e.target.value);
        break;
      default:
        return "";
    }
  }

  return (
    <div className="Signup">
      <h1>User Signup</h1>
      <form className="Signup-Form" onSubmit={handleSubmit}>
        <label className="label">Please enter your username.</label>
        <input
          value={username}
          name="username"
          type="text"
          className="input"
          onChange={handleChange}
        />

        <label type="email" className="label">
          Please enter your email.
        </label>
        <input
          value={email}
          name="email"
          type="email"
          className="input"
          onChange={handleChange}
        />

        <label className="label">Please create a password.</label>
        <input
          value={password}
          name="password"
          type="password"
          className="input"
          onChange={handleChange}
        />

        <label className="label">Confirm password.</label>
        <input
          value={passwordConfirmation}
          name="passwordConfirmation"
          type="password"
          className="input"
          onChange={handleChange}
        />

        <button type="submit">
          {isLoading ? "Loading" : "Create Account"}
        </button>
      </form>
      <h2 id="login">
        <Link to="/login">Already have an account? Login</Link>
      </h2>
    </div>
  );
}
