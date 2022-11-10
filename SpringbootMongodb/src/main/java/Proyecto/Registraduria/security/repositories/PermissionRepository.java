package Proyecto.Registraduria.security.repositories;

import Proyecto.Registraduria.security.models.Permission;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface PermissionRepository
        extends MongoRepository<Permission, String> {
}
