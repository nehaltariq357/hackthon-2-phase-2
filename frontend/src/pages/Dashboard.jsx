import React, { useState, useEffect } from 'react';
import TaskList from '../components/Tasks/TaskList';
import TaskForm from '../components/Tasks/TaskForm';
import { userAPI } from '../services/api';

const Dashboard = () => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchUserData();
  }, []);

  const fetchUserData = async () => {
    try {
      const response = await userAPI.getCurrentUser();
      setUser(response.data);
    } catch (err) {
      console.error('Failed to fetch user data:', err);
      // Redirect to login if unauthorized
      if (err.response?.status === 401) {
        localStorage.removeItem('access_token');
        window.location.href = '/login';
      }
    } finally {
      setLoading(false);
    }
  };

  const handleTaskCreated = () => {
    // Task created successfully - no specific action needed
    // TaskList will refresh on its own
  };

  if (loading) return <div>Loading dashboard...</div>;

  return (
    <div className="dashboard">
      <header className="dashboard-header">
        <h1>Welcome, {user?.email || 'User'}!</h1>
        <div className="user-actions">
          <button onClick={() => {
            localStorage.removeItem('access_token');
            window.location.href = '/login';
          }}>
            Logout
          </button>
        </div>
      </header>

      <main className="dashboard-main">
        <section className="task-creation">
          <TaskForm onTaskCreated={handleTaskCreated} />
        </section>

        <section className="task-list-section">
          <TaskList />
        </section>
      </main>
    </div>
  );
};

export default Dashboard;