import React, { useState } from 'react';

const TaskItem = ({ task, onUpdate, onDelete }) => {
  const [isEditing, setIsEditing] = useState(false);
  const [editData, setEditData] = useState({
    title: task.title,
    description: task.description || '',
    status: task.status,
    priority: task.priority,
    due_date: task.due_date || ''
  });

  const handleEditChange = (e) => {
    setEditData({
      ...editData,
      [e.target.name]: e.target.value
    });
  };

  const handleSaveEdit = async () => {
    try {
      await onUpdate(task.id, editData);
      setIsEditing(false);
    } catch (err) {
      console.error('Failed to update task:', err);
    }
  };

  const handleToggleComplete = async () => {
    try {
      const newStatus = task.status === 'completed' ? 'pending' : 'completed';
      await onUpdate(task.id, { ...editData, status: newStatus });
    } catch (err) {
      console.error('Failed to update task status:', err);
    }
  };

  return (
    <div className={`task-item ${task.status}`}>
      {isEditing ? (
        <div className="task-edit-form">
          <input
            type="text"
            name="title"
            value={editData.title}
            onChange={handleEditChange}
            required
          />
          <textarea
            name="description"
            value={editData.description}
            onChange={handleEditChange}
          />
          <select
            name="status"
            value={editData.status}
            onChange={handleEditChange}
          >
            <option value="pending">Pending</option>
            <option value="in_progress">In Progress</option>
            <option value="completed">Completed</option>
          </select>
          <select
            name="priority"
            value={editData.priority}
            onChange={handleEditChange}
          >
            <option value="low">Low</option>
            <option value="medium">Medium</option>
            <option value="high">High</option>
          </select>
          <input
            type="datetime-local"
            name="due_date"
            value={editData.due_date}
            onChange={handleEditChange}
          />
          <div className="edit-actions">
            <button onClick={handleSaveEdit}>Save</button>
            <button onClick={() => setIsEditing(false)}>Cancel</button>
          </div>
        </div>
      ) : (
        <div className="task-view">
          <div className="task-header">
            <input
              type="checkbox"
              checked={task.status === 'completed'}
              onChange={handleToggleComplete}
            />
            <h4 className={`task-title ${task.status === 'completed' ? 'completed' : ''}`}>
              {task.title}
            </h4>
          </div>

          {task.description && (
            <p className="task-description">{task.description}</p>
          )}

          <div className="task-meta">
            <span className={`priority priority-${task.priority}`}>
              {task.priority.charAt(0).toUpperCase() + task.priority.slice(1)}
            </span>
            <span className={`status status-${task.status}`}>
              {task.status.replace('_', ' ').charAt(0).toUpperCase() + task.status.slice(1).replace('_', ' ')}
            </span>
            {task.due_date && (
              <span className="due-date">Due: {new Date(task.due_date).toLocaleDateString()}</span>
            )}
          </div>

          <div className="task-actions">
            <button onClick={() => setIsEditing(true)}>Edit</button>
            <button onClick={() => onDelete(task.id)}>Delete</button>
          </div>
        </div>
      )}
    </div>
  );
};

export default TaskItem;