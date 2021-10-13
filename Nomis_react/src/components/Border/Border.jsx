import React from 'react';
import './Border.css';
import '../DropArea/DropArea.css';
import axios from 'axios';


function onChange(e) {
    let files = e.target.files;
    let reader = new FileReader();
    reader.readAsDataURL(files[0]);


    reader.onload=(e)=> {
        const url = "http://127.0.0.1:8000/api/taxengine/extract/"
        const formData = { file:e.target.result };
        console.log(e.target.result);
        return axios.post(url, formData, {name: "taxengine"}).then(response => console.warn("result", response));
    }
}

function Border() {

    const processes = ["Uploading File", "Pausing Queues", "Resume Queues", "Restarting API"];

    return (
        <div className="border">
            NOMIS
            <form method="post" className="drop_area" encType="multipart/form-data">
                <input type="file" name="file" onChange={(e)=>onChange(e)} />
            </form>
            <div className="status">
                Process Status
                <ul>
                    {processes.map((value, index) =>
                    <li key={index}>{value}</li>
                    )}
                </ul>
            </div>
        </div>)
};



export default Border;
