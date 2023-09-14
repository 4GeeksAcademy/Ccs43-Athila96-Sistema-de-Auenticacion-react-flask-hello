import React, { useContext } from "react";
import { Context } from "../store/appContext";
import rigoImageUrl from "../../img/rigo-baby.jpg";
import "../../styles/home.css";
import { SingUp } from "../component/singUp.jsx";
import { Login } from "../component/login.jsx";

export const Home = () => {
  const { store, actions } = useContext(Context);

  return (
    <div className="text-center vh-100 m-0 p-0">
      <Login />
    </div>
  );
};
