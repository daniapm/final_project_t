import React from 'react';
import './DropArea.css';

function onChange(e) {
    let files = e.target.files;
    let reader = new FileReader();
    reader.readAsDataURL(files[0]);
}

function DropArea() {
    return (
        <div className='drop_area'>
            <input type="file" name="file" onChange={(e)=>onChange(e)} />
        </div>)
};

export default DropArea;
