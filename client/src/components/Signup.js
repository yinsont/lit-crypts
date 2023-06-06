import React, {useState} from 'react'
import { Link } from "react-router-dom";
export default function Signup() {

const [firstName, setFirstName] = useState('');
const [lastName, setLastName] = useState('');

const [email, setEmail] = useState('');
const [password, setPassword] = useState('');
  return (
    <div className = "Signup">
      <h1>User Signup</h1>
        <form className = "Signup-Form">
          <label className="label">Please enter your first name.</label>
          <input value = {firstName}type="text" className="input" />

          <label className="label">Please enter your last name.</label>
          <input value = {lastName} type="text" className="input" />

          <label type ="email" className="label">Please enter your email.</label>
          <input value = {email} type ="email" className="input" />

          <label className="label">Please create a password.</label>
          <input value = {password} type="password" className="input" />
        </form>
      <h2 id = 'login'>
        <Link to="/login">Already have an account? Login</Link>
      </h2>
    </div>
  )
}