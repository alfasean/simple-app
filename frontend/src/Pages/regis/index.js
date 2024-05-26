import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import axios from 'axios';
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

function BasicExample() {
  const [name, setName] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate()
  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post('http://127.0.0.1:5000/account', {
        name,
        password
      });
      console.log(res.data);
      navigate('/login')
    } catch (error) {
      console.log(error);
    }
  }
  return (
    <div className='container'>
    <Form onSubmit={handleSubmit}>
      <Form.Group className="mb-3 mt-5" controlId="formBasicEmail">
        <Form.Label>Name</Form.Label>
        <Form.Control value={name} onChange={(e) => setName(e.target.value) } type="text" placeholder="Enter Your Name" />
      </Form.Group>

      <Form.Group className="mb-3" controlId="formBasicPassword">
        <Form.Label>Password</Form.Label>
        <Form.Control value={password} onChange={(e) => setPassword(e.target.value) } type="password" placeholder="Password" />
      </Form.Group>
      <Button variant="primary" type="submit">
        Submit
      </Button>
    </Form>
    </div>
  );
}

export default BasicExample;