package Proyecto.Registraduria.security.repositories;

import Proyecto.Registraduria.security.models.Role;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface RoleRepository
        extends MongoRepository<Role, String> {
}
