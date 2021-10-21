import React from 'react';
import './MainContainer.css'

const MainContainer = ({ children }) => {
    return (
        <section className="dsc-main-container">{children}
        </section >
    )
};

export default MainContainer;
