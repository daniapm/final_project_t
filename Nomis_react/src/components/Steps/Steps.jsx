import { Steps, Button, message } from 'antd';
import React from 'react'
import './Steps.css'


const { Step } = Steps;

export const steps = [
  {
    title: 'Tax file',
    content: 'Tax File',
    
  },
  {
    title: 'Update Dump',
    content: 'Second-content',
  },
  {
    title: 'Generate Mathops',
    content: 'Last-content',
  },
  {
    title: 'Lightweight file',
    content: 'Last-content',
  },
  {
    title: 'Configuration',
    content: 'Last-content',
  },
];
const StepComponent = () => {
  const [current, setCurrent] = React.useState(0);

  const next = () => {
    setCurrent(current + 1);
  };

  const prev = () => {
    setCurrent(current - 1);
  };

  return (
    <>
      <Steps current={current}>
        {steps.map(item => (
          <Step key={item.title} title={item.title} />
        ))}
      </Steps>
      <div className="steps-content">{steps[current].content}</div>
      <div className="steps-action">
        {current < steps.length - 1 && (
          <Button type="primary" onClick={() => next()}>
            Next
          </Button>
        )}
        {current === steps.length - 1 && (
          <Button type="primary" onClick={() => message.success('Processing complete!')}>
            Done
          </Button>
        )}
        {current > 0 && (
          <Button style={{ margin: '0 8px' }} onClick={() => prev()}>
            Previous
          </Button>
        )}
      </div>
    </>
  );
};

export default StepComponent;
