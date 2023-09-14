import React, { useContext, useState } from "react";
import { Context } from "../store/appContext";
import { Link } from "react-router-dom";

export const SingUp = () => {
  const { store, actions } = useContext(Context);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleCreteUser = async (event) => {
    event.preventDefault();
    actions.CreateUser(event, email, password);
  };

  return (
    <React.Fragment>
      <div className="container-fluid aa">
        <div className="row vh-100 align-items-center aa">
          <div className="col-8">
            <h1 className="text-info">
              <strong>SINGUP</strong>
            </h1>
            <form
              className="form-floating w-50 m-5 formu"
              onSubmit={handleCreteUser}
            >
              <div className="greeting mb-4">
                <h2>
                  <strong>Hello, friend!</strong>
                </h2>
              </div>
              <div className="form-floating mb-3 inputsDecoration">
                <input
                  type="email"
                  className="form-control styleInput"
                  id="floatingInput"
                  placeholder="name@example.com"
                  value={email}
                  onChange={(event) => {
                    setEmail(event.target.value);
                  }}
                />
                <label htmlFor="floatingInput" className="styleLabel">
                  <i className="fa-solid fa-envelope-open"></i>E-mail
                </label>
              </div>
              <div className="form-floating inputsDecoration">
                <input
                  type="password"
                  className="form-control styleInput"
                  id="floatingPassword"
                  placeholder="Password"
                  value={password}
                  onChange={(event) => {
                    setPassword(event.target.value);
                  }}
                />
                <label htmlFor="floatingPassword" className="styleLabel">
                  <i className="fa-solid fa-unlock-keyhole"></i>Password
                </label>
              </div>
              <div className="button button mb-0">
                <button type="submit" className="btn btn-primary mt-5 buttonss">
                  CREATE ACCOUNT
                </button>
              </div>
            </form>
            <div className="goRegister d-flex justify-contect-center">
              <Link to="/" className="m-0 p-0">
                <p className="" href="#" role="button">
                  If you already have an account. Login here
                </p>
              </Link>
            </div>
          </div>
          <div className="col-4 pageRight p-0">
            <div className="tilte m-5 mt-0">
              <h3 className="fs-1 text-white">Welcome</h3>
              <p className="text-white">
                Your attitude, not your aptitude, will determine your altitude.
              </p>
            </div>
          </div>
        </div>
      </div>
    </React.Fragment>
  );
};
