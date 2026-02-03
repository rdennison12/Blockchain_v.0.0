import React from 'react';
import { createBrowserRouter } from 'react-router-dom';
import App from './components/App';
import Blockchain from './components/Blockchain';
import ConductTransaction from './components/ConductTransaction';
import TransactionPool from './components/TransactionPool';

// React Router v6 router configuration
const router = createBrowserRouter([
  { path: '/', element: <App /> },
  { path: '/blockchain', element: <Blockchain /> },
  { path: '/conduct-transaction', element: <ConductTransaction /> },
  { path: '/transaction-pool', element: <TransactionPool /> }
]);

export default router;


