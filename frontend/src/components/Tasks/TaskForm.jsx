import React, { useState } from 'react';
import { taskAPI } from '../../services/api';

const TaskForm = ({ onTaskCreated }) => {
  const [formData, setFormData] = useState({
    title: '',
    description: '',
    priority: 'medium',
    due_date: ''
  });
  const [error, setError] = useState('');

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');

    try {
      const response = await taskAPI.createTask(formData);
      onTaskCreated(response.data);

      // Reset form
      setFormData({
        title: '',
        description: '',
        priority: 'medium',
        due_date: ''
      });
    } catch (err) {
      setError(err.response?.data?.detail || err.message || 'Failed to create task');
    }
  };

  return (
    <div className="task-form-container">
      <h3>Create New Task</h3>
      {error && <div className="error">{error}</div>}

      <form onSubmit={handleSubmit} className="task-form">
        <div className="form-group">
          <input
            type="text"
            name="title"
            placeholder="Task title"
            value={formData.title}
            onChange={handleChange}
            required
          />
        </div>

        <div className="form-group">
          <textarea
            name="description"
            placeholder="Task description"
            value={formData.description}
            onChange={handleChange}
          />
        </div>

        <div className="form-row">
          <div className="form-group">
            <select
              name="priority"
              value={formData.priority}
              onChange={handleChange}
            >
              <option value="low">Low Priority</option>
              <option value="medium">Medium Priority</option>
              <option value="high">High Priority</option>
            </select>
          </div>

          <div className="form-group">
            <input
              type="datetime-local"
              name="due_date"
              value={formData.due_date}
              onChange={handleChange}
            />
          </div>
        </div>

        <button type="submit">Create Task</button>
      </form>
    </div>
  );
};

export default TaskForm;