from src.db.db import db

class Blogs(db.Model):
    id = db.Column(db.String, primary_key=True)
    title = db.Column(db.String, nullable=False)
    slug = db.Column(db.String, unique=True, nullable=False)
    content = db.Column(db.String,nullable=False)
    category = db.Column(db.String,nullable=False)
    cover_url = db.Column(db.String,nullable=False)
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "slug": self.slug,
            "content": self.content,
            "category": self.category,
            "cover_url": self.cover_url
        }
 
