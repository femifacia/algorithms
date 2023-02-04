/*
** EPITECH PROJECT, 2020
** get_file_content
** File description:
** return a char * which is the content of the file of the path
*/

       #include <sys/types.h>
       #include <sys/stat.h>
       #include <unistd.h>
       #include <fcntl.h>
       #include <stdlib.h>


char *get_file_content(char *path)
{
    int fd = open(path, O_RDONLY);
    struct stat info;
    int check = 0;
    char *str = NULL;

    if (fd == -1)
        return (NULL);
    stat(path, &info);
    str = (char *)malloc(sizeof(char) * (info.st_size + 1));
    check = read(fd, str, info.st_size);
    str[info.st_size] = '\0';
    close(fd);
    if (check == -1) {
        free(str);
        return (NULL);
    }
    return (str);
}
