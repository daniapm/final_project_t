import React from 'react';
import './MainContent.css'

const MainContent = ({ children }) => {
    return (
        <section className="dsc-main-content">{children}
        </section >
    )
};

export default MainContent;
