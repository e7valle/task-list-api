from app import db


class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    completed_at = db.Column(db.DateTime, nullable=True)
    goal_id = db.Column(db.Integer, db.ForeignKey("goal.goal_id"), nullable=True)
    goal = db.relationship("Goal", back_populates="tasks")

    def to_result(self):
        is_complete = True 
        if not self.completed_at:
            is_complete = False 
        task_response = {
            "id":self.task_id,
            "title": self.title,
            "description": self.description,
            "is_complete": is_complete
        }

        if self.goal_id:
            task_response["goal_id"] = self.goal_id

        return task_response



