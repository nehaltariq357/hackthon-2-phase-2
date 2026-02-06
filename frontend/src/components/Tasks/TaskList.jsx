import React, { useState, useEffect } from 'react';
import { taskAPI } from '../../services/api';
import TaskItem from './TaskItem';

const TaskList = () => {
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    fetchTasks();
  }, []);

  const fetchTasks = async () => {
    try {
      setLoading(true);
      const response = await taskAPI.getTasks();
      setTasks(response.data);
    } catch (err) {
      setError(err.response?.data?.detail || err.message || 'Failed to fetch tasks');
    } finally {
      setLoading(false);
    }
  };

  const handleTaskUpdate = async (taskId, updatedTask) => {
    try {
      await taskAPI.updateTask(taskId, updatedTask);
      fetchTasks(); // Refresh the list
    } catch (err) {
      setError(err.response?.data?.detail || err.message || 'Failed to update task');
    }
  };

  const handleTaskDelete = async (taskId) => {
    try {
      await taskAPI.deleteTask(taskId);
      fetchTasks(); // Refresh the list
    } catch (err) {
      setError(err.response?.data?.detail || err.message || 'Failed to delete task');
    }
  };

  if (loading) return <div>Loading tasks...</div>;
  if (error) return <div className="error">Error: {error}</div>;

  return (
    <div className="task-list">
      <h3>Your Tasks</h3>
      {tasks.length === 0 ? (
        <p>No tasks found. Create your first task!</p>
      ) : (
        <div className="tasks-grid">
          {tasks.map(task => (
            <TaskItem
              key={task.id}
              task={task}
              onUpdate={handleTaskUpdate}
              onDelete={handleTaskDelete}
            />
          ))}
        </div>
      )}
    </div>
  );
};

export default TaskList;