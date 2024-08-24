import { Button, Tooltip } from "@chakra-ui/react";
import { Star, StarBorderOutlined } from "@mui/icons-material";
import React from "react";

type FavoriteButtonProps = {
    isClicked: Boolean;
    setIsClicked;
    color?: string;
};

export const FavoriteButton = ({
    isClicked,
    setIsClicked,
    color='yellow'
}: FavoriteButtonProps) => {
    const handleClick = (e: React.MouseEvent<HTMLButtonElement>) => {
        e.stopPropagation();
        setIsClicked(!isClicked);
    }
    return (
        <Button w='100%' color={color} variant='link' onClick={(e) => {handleClick(e)}}>
            <Tooltip label={'お気に入り-'+(isClicked? '解除': '登録')}>
                {isClicked? <Star/>: <StarBorderOutlined/>}
            </Tooltip>
        </Button>
    );
};

export default FavoriteButton;