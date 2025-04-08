
# 📘 Technical Documentation

## 🎬 Models Overview

### 👤 CustomUser (extends AbstractUser)
| Field         | Type          | Description                  |
|---------------|---------------|------------------------------|
| username      | CharField     | User's username              |
| email         | EmailField    | Email address                |
| is_moderator  | BooleanField  | Flag for moderator role      |
| created_at    | DateTimeField | Time of creation             |
| updated_at    | DateTimeField | Last update time             |

---

### 🏷️ Genre
| Field      | Type          | Description             |
|------------|---------------|-------------------------|
| name       | CharField     | Unique genre name       |
| created_at | DateTimeField | Time of creation        |
| updated_at | DateTimeField | Last update time        |

---

### 🎥 Movie
| Field        | Type              | Description                     |
|--------------|-------------------|---------------------------------|
| title        | CharField         | Movie title                     |
| description  | TextField         | Movie description               |
| release_date | DateField         | Release date                    |
| image        | ImageField        | Poster image                    |
| genres       | ManyToMany (Genre)| Related genres                  |
| created_at   | DateTimeField     | Time of creation                |
| updated_at   | DateTimeField     | Last update time                |

---

### 📝 Review
| Field      | Type             | Description                     |
|------------|------------------|---------------------------------|
| user       | ForeignKey(User) | Author of the review            |
| movie      | ForeignKey(Movie)| Reviewed movie                  |
| text       | TextField        | Review content                  |
| created_at | DateTimeField    | Time of creation (auto)         |
| updated_at | DateTimeField    | Last update time                |

> 🔐 Unique constraint: (user, movie)

---

### ⭐ Rating
| Field      | Type             | Description                     |
|------------|------------------|---------------------------------|
| user       | ForeignKey(User) | User who rated                  |
| movie      | ForeignKey(Movie)| Rated movie                     |
| score      | SmallInteger     | Score from 1 to 10              |
| created_at | DateTimeField    | Time of creation                |
| updated_at | DateTimeField    | Last update time                |

> 🔐 Unique constraint: (user, movie)

---

### ❤️ FavoriteMovie
| Field      | Type             | Description                     |
|------------|------------------|---------------------------------|
| user       | ForeignKey(User) | Who favorited                   |
| movie      | ForeignKey(Movie)| Favorited movie                 |
| created_at | DateTimeField    | Time of creation                |
| updated_at | DateTimeField    | Last update time                |

> 🔐 Unique constraint: (user, movie)

---

### 📚 UserMovieList
| Field      | Type               | Description                    |
|------------|--------------------|--------------------------------|
| user       | ForeignKey(User)   | Owner of the list              |
| name       | CharField          | List name                      |
| movies     | ManyToMany(Movie)  | Movies in the list             |
| created_at | DateTimeField      | Time of creation               |
| updated_at | DateTimeField      | Last update time               |

> 🔐 Unique constraint: (user, name)
